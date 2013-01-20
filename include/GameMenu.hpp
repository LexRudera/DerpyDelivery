#ifndef GAMEMENU_HPP
#define GAMEMENU_HPP

#include <Menu.hpp>
#include <boost\filesystem.hpp>
#include <MenuControls\Label.hpp>
#include <MenuControls\Button.hpp>

namespace me
{
    class GameMenu : public Menu
    {
        class GameSlot
        {
        public:
            GameSlot(const sf::String& Name, const boost::filesystem::path& Path);
            ~GameSlot();

            sf::String GetName() { return m_Name.GetString(); }
            sf::String GetPath() { return m_Path.string(); }
        private:
            Label m_Name;
            boost::filesystem::path m_Path;
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
            std::vector<GameSlot*> m_AvailableGames;
    };
}

#endif // GAMEMENU_HPP
