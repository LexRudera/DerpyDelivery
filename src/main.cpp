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

using namespace me;
int main()
{
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
