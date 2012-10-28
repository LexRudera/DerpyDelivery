#include "Game.hpp"
#include <iostream>
int main()
{
    tg::Game Derp;
    std::string EndMessage("OK");
    Derp.Run(EndMessage);
    Derp.GetWindow();
    if (EndMessage != "OK")
    {
        sf::err() << EndMessage;
        return 1;
    }
    else
        return 0;
}
