#include "Game.hpp"
#include "Input.hpp"

Game::Game()
{
    //ctor
}

Game::~Game()
{
    //dtor
}

void Game::Run(std::string& EndMessage) {
    m_window = new sf::RenderWindow(sf::VideoMode(800,600),"Some Game");
    while (m_window->isOpen())
    {
        // Process events
        sf::Event event;
        while (m_window->pollEvent(event))
        {
        // Close window : exit
        if (event.type == sf::Event::Closed)
        m_window->close();
        }
        // Clear screen
        m_window->clear();
        // Update the window
        m_window->display();
    }
}
