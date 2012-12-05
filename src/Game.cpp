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
        //Log("Initializing");
        Game::sm_frameTime = m_clk.restart();
        m_window = new sf::RenderWindow(sf::VideoMode(800,600),"Some Game",sf::Style::Titlebar);
        ChangeScene(scn);

        sf::Event event;
        sf::Text FpsTxt;
        FpsTxt.setCharacterSize(20);
        FpsTxt.setFont(*GetResourceManager()->GetFont("Gentium"));
        //Log("Initialized");
        while (m_window->isOpen())
        {
            // Input/events
            //--------------
            //Log("Input");
            while (m_window->pollEvent(event))
            {
                // Close window : exit
                if (event.type == sf::Event::Closed)
                    m_window->close();
            }
            if (Input::Keyboard::IsKeyPressed(sf::Keyboard::Key::Escape))
                m_window->close();
            //Log("Inputed?");

            // Logic
            //-------
            //Log("Tick");
            GetActiveScene()->Tick();
            //Log("Ticked");

            // Render
            //--------
            //Log("Render");
            m_window->clear( );
            GetActiveScene()->Render(*m_window);

            if (GetConfiguration()->ShowFps())
            {
                FpsTxt.setString(to_string(1/Game::sm_frameTime.asSeconds()));
                m_window->draw(FpsTxt);
            }
            m_window->display();
            //Log("Rendered");

            // After frame stuff
            //-------------------
            //Log("After");
            Game::sm_frameTime = m_clk.restart();
            //Log("Aftered");
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
