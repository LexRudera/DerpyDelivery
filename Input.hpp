#ifndef INPUT_H
#define INPUT_H
#include <vector>
#include "Game.hpp"

namespace tg
{
    class Input
    {
        public:
            class Keyboard
            {
                public:
                    static bool IsKeyPressed(sf::Keyboard::Key k) { return sf::Keyboard::isKeyPressed(k); }
                protected:
                private:
            };

            class Mouse
            {
                public:
                    static bool isButtonPressed(sf::Mouse::Button b) { return sf::Mouse::isButtonPressed(b); }
                    static sf::Vector2i getPosition() { return sf::Mouse::getPosition(); }
                    static sf::Vector2i getPosition(const sf::Window &relativeTo) { return sf::Mouse::getPosition(relativeTo); }
                    static void setPosition (const sf::Vector2i &position) { sf::Mouse::setPosition(position); }
                    static void setPosition (const sf::Vector2i &position, const sf::Window &relativeTo) { sf::Mouse::setPosition(position, relativeTo); }
                protected:
                private:
            };
        protected:
        private:
    };
};

#endif // INPUT_H
