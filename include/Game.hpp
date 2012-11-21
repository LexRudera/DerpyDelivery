#ifndef GAME_H
#define GAME_H

#include <string>
#include <SFML/Graphics.hpp>
#include "Scene.hpp"

namespace me
{
    class Game
    {
        public:
            /** Default constructor */
            Game();
            /** Default destructor */
            virtual ~Game();
            void Run(std::string& EndMessage);
            sf::RenderWindow* GetWindow() const {return m_window;}
            me::Scene* GetActiveScene() const {return m_activeScene;}
            void ChangeScene(me::Scene* scn);

            sf::Time* GetFrameTime() { return &me::Game::sm_frameTime; }
        protected:
        private:
            sf::Clock m_clk;
            sf::RenderWindow* m_window;
            me::Scene* m_activeScene;

            static sf::Time sm_frameTime;
    };
};

#endif // GAME_H
