#include "GameMenu.hpp"
#include "Game.hpp"
#include "MainMenu.hpp"
#include "Global.hpp"
#include <boost/filesystem.hpp>
#include <boost/algorithm/string/case_conv.hpp>
#include <fstream>

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
        //Game::Get()->ChangeScene(new MainMenu());
        Add(m_BackBtn = new Button(this,"<-",sf::Vector2f(100,Game::Get()->GetWindow()->getSize().y-50),sf::Vector2f(25,25)));

        // Create the slots
        const unsigned int& Slots = m_AvailableGames.size();
        const unsigned int height = 80;
        const unsigned int space = 25;
        for (unsigned int i = 0; i < Slots; i++)
        {
            Log("Slot no. " + to_string(i+1));
            //Add(sf::Vector2f(Game::Get()->GetWindow()->getSize().x-175, height), sf::Vector2f(150, Game::Get()->GetWindow()->getSize().y/2 +(height+space)*i - (height*Slots + space* (Slots-1))/2 ));
            m_AvailableGames[i].Box->setPosition(sf::Vector2f(150, Game::Get()->GetWindow()->getSize().y/2 +(height+space)*i - (height*Slots + space* (Slots-1))/2 ));
            m_AvailableGames[i].Box->setSize(sf::Vector2f(Game::Get()->GetWindow()->getSize().x-175, height));
        }
        //Log(Game::Get()->GetWindow()->getSize().y/2-50);
        //Add(new StaticBox(sf::Vector2f(Game::Get()->GetWindow()->getSize().x-175,100), sf::Vector2f(150, Game::Get()->GetWindow()->getSize().y/2-50 -50-25/2) ));

        //Add(new StaticBox( sf::Vector2f(Game::Get()->GetWindow()->getSize().x-175,100), sf::Vector2f(150, Game::Get()->GetWindow()->getSize().y/2-50 +50+25/2) ));
        //Add(new StaticBox(sf::Vector2f(300,100), sf::Vector2f(150,100)));
        //Add(new StaticBox(sf::Vector2f(300,100), sf::Vector2f(150,100)));

        //StaticBox Slot
        //Label Name
        //Button NewGame
        //Selector Saves
        //Button LoadSave
        //Button DeleteSave

        m_BackBtn->SetOnClickFunction(static_cast<MenuEvent>(&GameMenu::m_BackBtn_OnClick));
        Log("--GAMEMENU END--");
    }
    void GameMenu::ScanGameFolder() {
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
                Log("  Folder found");
                //Scanning the directory
                bool valid = false;
                for (boost::filesystem::directory_iterator o = boost::filesystem::directory_iterator(i->path()); o != end; ++o)
                {
                    // Is it the GameInfo.txt file?
                    if (boost::algorithm::to_lower_copy(o->path().filename().string()) == "gameinfo.txt")
                    {
                        Log("    GameInfo Found");
                        valid = true;
                        counter++;
                        break;
                    }
                }
                // Is it a valid directory? Ie. did it find a GameInfo.txt in the folder?
                if (!valid)
                {
                    Log("    GameInfo not found. Invalid Game Folder");
                }
            }
        }
    }
    void GameMenu::LoadGameInfo(unsigned int index) {
        std::fstream InfoFile(m_AvailableGames[index]->GetPath() + "\\GameInfo.txt");
    }

    void GameMenu::m_BackBtn_OnClick()
    {
        Game::Get()->ChangeScene(new MainMenu());
    }

    GameMenu::GameSlot::GameSlot(const sf::String& aName, const boost::filesystem::path& aPath)
    : m_Name(aName),
    m_Path(aPath)
    {

    }
}

