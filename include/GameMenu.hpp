#ifndef GAMEMENU_HPP
#define GAMEMENU_HPP

#include <Menu.hpp>
#include <boost\filesystem.hpp>
#include "MenuControls.hpp"

namespace me
{
    class GameMenu : public Menu
    {
        class GameSlot : public ControlBase
        {
        public:
            GameSlot(const sf::String& Name, const boost::filesystem::path& Path);
            ~GameSlot();

            void draw(sf::RenderTarget& target, sf::RenderStates states) const;

            sf::String GetName() { return m_Name.GetString(); }
            sf::String GetPath() { return m_Path.string(); }

            void SetSize(const sf::Vector2f& size) { m_Box.SetSize(size); }
            void SetSize(float x, float y) { m_Box.SetSize(sf::Vector2f(x,y)); }
            sf::Vector2f GetSize() { return m_Box.GetSize(); }
            void GetSize(float* x, float* y) { *x = m_Box.GetSize().x; *y = m_Box.GetSize().y; }
        private:
            StaticBox m_Box;
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
