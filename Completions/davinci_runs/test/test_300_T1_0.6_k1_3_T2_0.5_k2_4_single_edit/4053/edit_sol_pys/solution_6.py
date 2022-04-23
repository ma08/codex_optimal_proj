/*
 * Copyright (c) 2016, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.  Oracle designates this
 * particular file as subject to the "Classpath" exception as provided
 * by Oracle in the LICENSE file that accompanied this code.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Please contact Oracle, 500 Oracle Parkway, Redwood Shores, CA 94065 USA
 * or visit www.oracle.com if you need additional information or have any
 * questions.
 */

package jdk.internal.module;

import java.io.IOException;
import java.io.InputStream;
import java.io.UncheckedIOException;
import java.lang.module.ModuleDescriptor;
import java.lang.module.ModuleDescriptor.Requires.Modifier;
import java.lang.module.ModuleDescriptor.Version;
import java.lang.module.ModuleFinder;
import java.lang.module.ModuleReference;
import java.lang.module.ModuleReader;
import java.lang.module.ModuleReader.Index;
import java.lang.module.ModuleReader.IndexEntry;
import java.lang.module.ModuleReader.IndexGroup;
import java.lang.module.ModuleReader.IndexGroupEntry;
import java.lang.module.ModuleReader.IndexReader;
import java.lang.module.ModuleReader.IndexTree;
import java.lang.module.ModuleReader.IndexTreeEntry;
import java.lang.module.ModuleReference.Attributes;
import java.lang.module.ModuleReference.Builder;
import java.lang.module.ModuleReference.Requires;
import java.lang.module.ModuleReference.Provides;
import java.lang.module.ModuleReference.Exports;
import java.lang.module.ModuleReference.Opens;
import java.lang.module.ModuleReference.Conceals;
import java.lang.module.ModuleReference.MainClass;
import java.lang.module.ModuleReference.Target;
import java.lang.module.ModuleReference.VersionedTarget;
import java.lang.module.ModuleReference.CompiledVersion;
import java.lang.module.ModuleReference.Requires.Modifier;
import java.lang.module.ModuleReference.Exports.Target;
import java.lang.module.ModuleReference.Opens.Target;
import java.lang.module.ModuleReference.Conceals.Target;
import java.lang.module.ModuleReference.CompiledVersion.Version;
import java.lang.module.ModuleReference.CompiledVersion.Target;
import java.lang.module.ModuleReference.CompiledVersion.VersionedTarget;
import java.lang.module.ModuleReference.CompiledVersion.VersionedTarget.Version;
import java.lang.module.ModuleReference.CompiledVersion.VersionedTarget.Target;
import java.lang.module.ModuleReference.CompiledVersion.VersionedTarget.Target.Version;
import java.lang.module.ModuleReference.CompiledVersion.VersionedTarget.Target.Target;
import java.net.URI;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import jdk.internal.org.objectweb.asm.ClassReader;
import jdk.internal.org.objectweb.asm.ClassVisitor;
import jdk.internal.org.objectweb.asm.FieldVisitor;
import jdk.internal.org.objectweb.asm.Opcodes;
import jdk.internal.org.objectweb.asm.Type;

import static jdk.internal.org.objectweb.asm.Opcodes.ASM6;

/**
 * Utility to read the module-info.class file.
 */

public final class ModuleInfo {

    private ModuleInfo() { }

    public static ModuleDescriptor read(Path path) {
        try (InputStream in = Files.newInputStream(path)) {
            return read(in);
        } catch (IOException ioe) {
            throw new UncheckedIOException(ioe);
        }
    }

    public static ModuleDescriptor read(InputStream in) {
        return new ClassFileReader(in).read();
    }

    private static final class ClassFileReader {
        private final InputStream in;
        private ModuleDescriptor.Builder builder;
        private Set<String> packages;
        private ModuleDescriptor descriptor;

        ClassFileReader(InputStream in) {
            this.in = in;
        }

        ModuleDescriptor read() {
            new ClassReader(in).accept(new ClassVisitor(ASM6) {
                @Override
                public void visit(int version, int access, String name,
                                  String signature, String superName,
                                  String[] interfaces)
                {
                    if (!name.equals("module-info")) {
                        throw new IllegalArgumentException("Not a module-info.class file");
                    }
                }

                @Override
                public FieldVisitor visitField(int access, String name,
                                               String descriptor, String signature,
                                               Object value)
                {
                    if (name.equals("module_version")) {
                        if (!descriptor.equals("Ljava/lang/String;")) {
                            throw new IllegalArgumentException("Invalid module_version field");
                        }
                        Optional<String> version = Optional.ofNullable((String)value);
                        builder.version(version.map(Version::parse));
                    }
                    return null;
                }
            }, ClassReader.SKIP_CODE | ClassReader.SKIP_DEBUG | ClassReader.SKIP_FRAMES);
            return descriptor;
        }
    }

}
