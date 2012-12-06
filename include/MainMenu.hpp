#ifndef MAINMENU_H
#define MAINMENU_H

#include <Menu.hpp>
#include "MenuControls/Label.hpp"
#include "MenuControls/Image.hpp"
#include "MenuControls/Button.hpp"

namespace me
{
    class MainMenu : public Menu
    {
        public:
            MainMenu();
            virtual ~MainMenu();
            sf::String GetType() const { return "MainMenu"; }
        protected:
        private:
            Label* Title;
            Image* ComplementaryPicture;
            Button* PlayBtn;
            Button* OptionsBtn;
            Button* QuitBtn;

            void Quit_OnClick();
    };
}
#endif // MAINMENU_H
