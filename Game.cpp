#include "Game.hpp"
#include "Input.hpp"

tg::Game::Game() {
    //ctor
}

tg::Game::~Game() {
    //dtor
}

void tg::Game::Run(std::string& EndMessage) {
    m_window = new sf::RenderWindow(sf::VideoMode(800,600),"Some Game");
    ChangeScene(new tg::Scene());
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
        m_frameTime = m_clk.restart().asMilliseconds();
    }
    return;
}
void tg::Game::ChangeScene(tg::Scene* scn) {
    delete m_activeScene;
    m_activeScene = scn;
    return;
}
