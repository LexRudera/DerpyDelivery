#ifndef GAME_H
#define GAME_H
#include <string>
#include <SFML/Graphics.hpp>

class Game
{
    public:
        /** Default constructor */
        Game();
        /** Default destructor */
        virtual ~Game();
        void Run(std::string& EndMessage);
        sf::RenderWindow* GetWindow() const {return m_window;}
        void Fun();
    protected:
    private:
        sf::RenderWindow* m_window;
};

#endif // GAME_H
