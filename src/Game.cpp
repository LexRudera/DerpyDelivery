#include "Game.hpp"
#include "Input.hpp"
#include <iostream>

namespace me
{
    sf::Time Game::sm_frameTime;
    Game* Game::sm_Instance;

    Game::Game() {
        m_activeScene = 0;
        Game::sm_Instance = this;
    }

    Game::Game(Settings* conf) : Game()
    {
        m_config = conf;
    }

    Game::~Game() {
    }

    void Game::Run(std::string& EndMessage, Scene* scn) {
        m_window = new sf::RenderWindow(sf::VideoMode(800,600),"Some Game");
        ChangeScene(scn);
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
            if (Input::Keyboard::IsKeyPressed(sf::Keyboard::Key::Escape))
                m_window->close();

            // Logic
            //-------
            GetActiveScene()->Tick();

            // Render
            //--------
            m_window->clear();
            GetActiveScene()->Render(*m_window);
            m_window->display();

            // After frame stuff
            //-------------------
            Game::sm_frameTime = m_clk.restart();
            if (GetConfiguration()->ShowFps())
            {

            }
        }
        delete m_window;
        return;
    }
    void Game::ChangeScene(Scene* scn) {
        if (m_activeScene != 0)
        {
            delete m_activeScene;
            //m_activeScene = 0;
        }
        m_activeScene = scn;
        return;
    }
}
