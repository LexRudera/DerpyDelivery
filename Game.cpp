#include "Game.hpp"
#include "Input.hpp"
#include <iostream>

sf::Time me::Game::sm_frameTime;

me::Game::Game() {
    //ctor
    m_activeScene = 0;
}

me::Game::~Game() {
    //dtor
}

void me::Game::Run(std::string& EndMessage) {
    m_window = new sf::RenderWindow(sf::VideoMode(800,600),"Some Game");
    ChangeScene(new me::Scene());
    while (m_window->isOpen())
    {
        // Input/events
        //--------------
        sf::Event event;
        while (m_window->pollEvent(event))
        {
            // Close window : exit
            if (event.type == sf::Event::Closed)
                m_window->close();
        }

        // Logic
        //-------
        GetActiveScene()->Tick();

        // Render
        //--------
        m_window->clear();
        GetActiveScene()->Render();
        m_window->display();

        // After frame stuff
        //-------------------
        me::Game::sm_frameTime = m_clk.restart();
    }
    return;
}
void me::Game::ChangeScene(me::Scene* scn) {
    if (m_activeScene != 0)
    {
        delete m_activeScene;
        m_activeScene = 0;
    }
    m_activeScene = scn;
    return;
}
