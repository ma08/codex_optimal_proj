#!/usr/bin/env ruby

require 'rubygems'
require 'find'
require 'sqlite3'

# This is a simple file indexer.
# It will walk through the given directory and index everything in a sqlite3 database.
# The database will be created if it doesn't exist.
#
# TODO:
#   - Add support for multiple directories
#   - Add support for file types
#   - Add support for indexing only certain file types
#   - Add support for indexing only certain directories
#   - Add support for indexing only certain file names
#   - Add support for indexing only certain file contents
#   - Add support for indexing only certain file sizes
#   - Add support for indexing only certain file dates
#   - Add support for indexing only certain file owners
#   - Add support for indexing only certain file groups
#   - Add support for indexing only certain file permissions
#   - Add support for indexing only certain file attributes
#   - Add support for indexing only certain file inodes
#   - Add support for indexing only certain file hard links
#   - Add support for indexing only certain file symbolic links
#   - Add support for indexing only certain file devices
#   - Add support for indexing only certain file sockets
#   - Add support for indexing only certain file pipes
#   - Add support for indexing only certain file character devices
#   - Add support for indexing only certain file block devices
#   - Add support for indexing only certain file executables
#   - Add support for indexing only certain file readable
#   - Add support for indexing only certain file writable
#   - Add support for indexing only certain file executable
#   - Add support for indexing only certain file empty
#   - Add support for indexing only certain file size 0

# The root directory to crawl
root_dir = ARGV[0]

# The database file to use
db_file = ARGV[1]

# Create the database if it doesn't exist
if !File.exists?(db_file)
  db = SQLite3::Database.new(db_file)
  db.execute("CREATE TABLE files (path TEXT, name TEXT, size INTEGER, date TEXT, owner TEXT, group TEXT, permissions TEXT, attributes TEXT, inode INTEGER, hard_links INTEGER, symbolic_links INTEGER, device INTEGER, socket INTEGER, pipe INTEGER, character_device INTEGER, block_device INTEGER, executable INTEGER, readable INTEGER, writable INTEGER, empty INTEGER)")
  db.execute("CREATE UNIQUE INDEX files_path ON files(path)")
  db.execute("CREATE INDEX files_name ON files(name)")
  db.execute("CREATE INDEX files_size ON files(size)")
  db.execute("CREATE INDEX files_date ON files(date)")
  db.execute("CREATE INDEX files_owner ON files(owner)")
  db.execute("CREATE INDEX files_group ON files(group)")
  db.execute("CREATE INDEX files_permissions ON files(permissions)")
  db.execute("CREATE INDEX files_attributes ON files(attributes)")
  db.execute("CREATE INDEX files_inode ON files(inode)")
  db.execute("CREATE INDEX files_hard_links ON files(hard_links)")
  db.execute("CREATE INDEX files_symbolic_links ON files(symbolic_links)")
  db.execute("CREATE INDEX files_device ON files(device)")
  db.execute("CREATE INDEX files_socket ON files(socket)")
  db.execute("CREATE INDEX files_pipe ON files(pipe)")
  db.execute("CREATE INDEX files_character_device ON files(character_device)")
  db.execute("CREATE INDEX files_block_device ON files(block_device)")
  db.execute("CREATE INDEX files_executable ON files(executable)")
  db.execute("CREATE INDEX files_readable ON files(readable)")
  db.execute("CREATE INDEX files_writable ON files(writable)")
  db.execute("CREATE INDEX files_empty ON files(empty)")
  db.close
end

# Open the database
db = SQLite3::Database.new(db_file)

# Walk the root directory and index each file
Find.find(root_dir) do |path|
  if File.file?(path)
    # Get the file info
    name = File.basename(path)
    size = File.size(path)
    date = File.mtime(path)
    owner = File.stat(path).uid
    group = File.stat(path).gid
    permissions = File.stat(path).mode
    attributes = File.stat(path).blksize
    inode = File.stat(path).ino
    hard_links = File.stat(path).nlink
    symbolic_links = File.symlink?(path) ? 1 : 0
    device = File.stat(path).dev
    socket = File.socket?(path) ? 1 : 0
    pipe = File.pipe?(path) ? 1 : 0
    character_device = File.chardev?(path) ? 1 : 0
    block_device = File.blockdev?(path) ? 1 : 0
    executable = File.executable?(path) ? 1 : 0
    readable = File.readable?(path) ? 1 : 0
    writable = File.writable?(path) ? 1 : 0
    empty = size == 0 ? 1 : 0

    # Insert the file info into the database
    db.execute("INSERT OR REPLACE INTO files (path, name, size, date, owner, group, permissions, attributes, inode, hard_links, symbolic_links, device, socket, pipe, character_device, block_device, executable, readable, writable, empty) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", path, name, size, date, owner, group, permissions, attributes, inode, hard_links, symbolic_links, device, socket, pipe, character_device, block_device, executable, readable, writable, empty) unless db.nil?
  end
end

# Close the database
db.close
