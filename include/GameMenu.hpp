#ifndef GAMEMENU_HPP
#define GAMEMENU_HPP

#include <Menu.hpp>

namespace me
{
    class GameMenu : public Menu
    {
        class m_GameSlot
        {
        };
        public:
            /** Default constructor */
            GameMenu();
            /** Default destructor */
            virtual ~GameMenu();

            void Load();
        protected:
        private:
            void ScanGameFolder();
            void LoadGameInfo();
            std::vector<m_GameSlot> m_GameSelections;
    };
}

#endif // GAMEMENU_HPP
