#ifndef GAME_H
#define GAME_H

#include <string>
#include <SFML/Graphics.hpp>
#include "Settings.hpp"
#include "Scene.hpp"

namespace me
{
    class Game
    {
        public:
            Game(Settings* conf);
            virtual ~Game();
            void Run(std::string& EndMessage, Scene* scn);
            sf::RenderWindow* GetWindow() const {return m_window;}
            me::Scene* GetActiveScene() const {return m_activeScene;}
            void ChangeScene(me::Scene* scn);

            sf::Time* GetFrameTime() { return &Game::sm_frameTime; }
            Settings* GetConfiguration() { return m_config; }
            static void Quit() {Game::sm_Instance->GetWindow()->close();}
        protected:
        private:
            Game();
            Settings* m_config;
            sf::Clock m_clk;
            sf::RenderWindow* m_window;
            me::Scene* m_activeScene;

            static sf::Time sm_frameTime;
            static Game* sm_Instance;
    };
};

#endif // GAME_H
