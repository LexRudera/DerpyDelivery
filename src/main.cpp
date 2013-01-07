//---------------------------------------------
// Derpy Delivery
// Mail Engine based on SFML
// Programmed by Lex Rudera - lex@pulsewave.co
// zlib licence
//---------------------------------------------

#include "Game.hpp"
#include "Settings.hpp"
#include "MainMenu.hpp"
#include "Global.hpp"
#include <iostream>
#include <boost/filesystem.hpp>

using namespace me;
int main()
{

        boost::filesystem::path GameDir = boost::filesystem::current_path();
        //GameDir += "\\.";
        Log(GameDir.string());

    //boost::filesystem::path CurrentPath = boost::filesystem::current_path();
    //Log(CurrentPath.string());
    //for (boost::filesystem::path::iterator i = GameDir.begin(); i != GameDir.end(); i++)
    //    Log(i->string());
    for (boost::filesystem::directory_iterator i = boost::filesystem::directory_iterator(GameDir).begin(); i != boost::filesystem::directory_iterator(GameDir).end(); i++)
        Log(i->string());

    Log("");
    Log("Running");
    Log("Setting up game instance");
    Game Derp(new Settings());
    std::string EndMessage("OK");
    Log("Firing up the game.");

    Derp.Run(EndMessage, new MainMenu());
    if (EndMessage != "OK")
    {
        Error(EndMessage);
        return 1;
    }
    else
        return 0;
}
