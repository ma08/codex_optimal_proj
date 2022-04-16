//
// Created by kier on 2019/1/25.
//

#ifndef TENSORSTACK_FILE_H
#define TENSORSTACK_FILE_H

#include <string>
#include <fstream>

namespace ts {
    namespace file {
        bool is_exist(const std::string &path);

        void create_dir(const std::string &path);

        void remove_dir(const std::string &path);

        void remove_file(const std::string &path);

        std::fstream append_file(const std::string &path);
    }
}


#endif //TENSORSTACK_FILE_H
