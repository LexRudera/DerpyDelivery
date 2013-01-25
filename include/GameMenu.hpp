#ifndef GAMEMENU_HPP
#define GAMEMENU_HPP

#include <Menu.hpp>
#include <boost\filesystem.hpp>
#include "MenuControls.hpp"

namespace me
{
    class GameMenu : public Menu
    {
        struct GameSlot
        {
            StaticBox* Box;
            Label* Name;
            Button* Btn;
            boost::filesystem::path Path;
        };

        public:
            GameMenu();
            virtual ~GameMenu();

            void Load();
        protected:
        private:
            void ScanGameFolder();
            void LoadGameInfo(unsigned int);

            void m_BackBtn_OnClick();

            Button* m_BackBtn;

            std::vector<GameSlot> m_AvailableGames;
    };
}

#endif // GAMEMENU_HPP
