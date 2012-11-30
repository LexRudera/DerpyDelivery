#include "Global.hpp"
#include "Game.hpp"
#include <sstream>

namespace me
{
    void Error(std::string err)
    {
        std::cerr << err << std::endl;
    }
    void CriticalError(std::string err)
    {
        std::cerr << err << std::endl;
        int i;
        std::cin >> i;
        me::Game::Quit();
    }
    void Log(std::string txt)
    {
        std::cout << txt << std::endl;
    }

    template <typename T>
    std::string to_string (const T& t)
    {
        std::stringstream ss;
        ss << t;
        return ss.str();
    }
}
