#ifndef SELECTEDGAMEMENU_H
#define SELECTEDGAMEMENU_H

#include <Menu.hpp>
#include <boost\filesystem.hpp>
#include "MenuControls.hpp"

namespace me
{
    class SelectedGameMenu : public Menu
    {
        public:
            SelectedGameMenu(const boost::filesystem::path& path);
            virtual ~SelectedGameMenu();

            void Load();
        protected:
        private:
            StaticBox* m_Box;

            Label* m_Title;
            Label* m_SubTitle;
            Label* m_Author;
            Label* m_Email;
            Label* m_Website;
            Label* m_Description;

            Selector* m_Saves;

            Button* m_Back;
            Button* m_Load;
            Button* m_Delete;
            Button* m_Play;
    };
}

#endif // SELECTEDGAMEMENU_H
