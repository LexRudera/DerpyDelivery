//---------------------------------------------
// Derpy Delivery
// Mail Engine based on SFML
// Programmed by Lex Rudera - lex@pulsewave.co
// zlib licence
//---------------------------------------------

#include "Game.hpp"
#include "Settings.hpp"
#include "Menu.hpp"
#include "Global.hpp"
#include <iostream>

int main()
{
    me::Game Derp(new me::Settings());
    std::string EndMessage("OK");
    Derp.Run(EndMessage, me::Menu::MainMenu());
    if (EndMessage != "OK")
    {
        me::Error(EndMessage);
        return 1;
    }
    else
        return 0;
}
