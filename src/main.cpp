//---------------------------------------------
// Derpy Delivery
// Mail Engine based on SFML
// Programmed by Lex Rudera - lex@pulsewave.co
// zlib licence
//---------------------------------------------

#include "Game.hpp"
#include <iostream>
int main()
{
    me::Game Derp;
    std::string EndMessage("OK");
    Derp.Run(EndMessage);
    if (EndMessage != "OK")
    {
        sf::err() << EndMessage;
        return 1;
    }
    else
        return 0;
}