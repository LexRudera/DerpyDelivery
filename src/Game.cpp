#include "Game.hpp"
#include "Input.hpp"
#include <iostream>
#include "Global.hpp"

namespace me
{
    sf::Time Game::sm_frameTime;
    Game* Game::sm_Instance;

    Game::Game() {
        Game::sm_Instance = this;
        m_activeScene = 0;
        m_ResManager = new ResourceManager();
        GetResourceManager()->LoadFont("Gentium", "Gentium-R.ttf");
    }

    Game::Game(Settings* conf) : Game()
    {
        m_config = conf;
    }

    Game::~Game() {
        delete m_config;
        delete m_ResManager;
    }

    void Game::Run(std::string& EndMessage, Scene* scn) {
        m_window = new sf::RenderWindow(sf::VideoMode(800,600),"Some Game");
        ChangeScene(scn);

        sf::Event event;
        while (m_window->isOpen())
        {
            // Input/events
            //--------------
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
            m_window->clear( );
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
        Log("Changing scene");
        m_activeScene = scn;
        return;
    }
}
