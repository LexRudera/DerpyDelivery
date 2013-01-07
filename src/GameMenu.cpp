#include "GameMenu.hpp"
#include <boost/filesystem.hpp>

namespace me
{
    GameMenu::GameMenu()
    {
        //ctor
    }

    GameMenu::~GameMenu()
    {
        //dtor
    }

    void GameMenu::Load()
    {
        // Scan game folder
        boost::filesystem::path GameDir = boost::filesystem::current_path();
        GameDir += "\\games";
        /*for (boost::filesystem::path::iterator it = Current;;)
        {

        }*/
    }
}

