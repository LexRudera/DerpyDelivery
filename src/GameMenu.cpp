#include "GameMenu.hpp"
#include "Game.hpp"
#include "MainMenu.hpp"
#include "Global.hpp"
#include <boost/filesystem.hpp>
#include <boost/algorithm/string/case_conv.hpp>

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
        Log("--GAMEMENU START--");
        ScanGameFolder();
        Game::Get()->ChangeScene(new MainMenu());
        Log("--GAMEMENU END--");
    }
    void GameMenu::ScanGameFolder()
    {
        // Scan game folder
        boost::filesystem::path GameDir = boost::filesystem::current_path();
        GameDir += "\\games";

        // Iterate through them to find games
        unsigned int counter = 0; // We need to know how many games there actually are
        boost::filesystem::directory_iterator end; // End iterator. Weird.
        // Scanning GameFolder
        for (boost::filesystem::directory_iterator i = boost::filesystem::directory_iterator(GameDir); i != end; ++i)
        {
            // Is it a directory?
            if(boost::filesystem::is_directory(i->path()))
            {
                //Scanning the directory
                bool valid = false;
                for (boost::filesystem::directory_iterator o = boost::filesystem::directory_iterator(i->path()); o != end; ++o)
                {
                    // Is it the GameInfo.txt file?
                    if (boost::algorithm::to_lower_copy(o->path().filename().string()) == "gameinfo.txt")
                    {
                        Log("GameInfo Found");
                        valid = true;
                        counter++;
                        break;
                    }
                }
                // Is it a valid directory? Ie. did it find a GameInfo.txt in the folder?
                if (!valid)
                {
                    Log("GameInfo not found. Invalid Game Folder");
                    invalid++;
                }
            }
        }
    }
    void GameMenu::ReadInfo()
}

