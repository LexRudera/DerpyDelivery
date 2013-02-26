#include "SelectedGameMenu.hpp"
#include "Game.hpp"
#include "GameMenu.hpp"
#include "Global.hpp"
#include <fstream>
#include <regex>
#include <boost/algorithm/string/case_conv.hpp>
#include "Utils/GameInfoReader.hpp"

namespace me
{
    SelectedGameMenu::SelectedGameMenu(const boost::filesystem::path& path)
    {
        m_Path = path;
    }

    SelectedGameMenu::~SelectedGameMenu()
    {

    }

    void SelectedGameMenu::Load()
    {
        GameInfoReader GIF(m_Path.string() + "\\gameinfo.txt");
        // Element creation
        sf::Vector2f Size = sf::Vector2f((Game::Get()->GetWindow()->getSize().y-30)/3*4, (Game::Get()->GetWindow()->getSize().y-30));
        sf::Vector2f TopLeftPos = sf::Vector2f(Game::Get()->GetWindow()->getSize().x/2-Size.x/2,15);
        Add(m_Box = new StaticBox(Size, TopLeftPos));
        Add(m_Title = new Label(GIF.Read("title"), 50, TopLeftPos + sf::Vector2f(80,30)));
        Add(m_SubTitle = new Label(GIF.Read("Subtitle"), 25, TopLeftPos + sf::Vector2f(90,80)));
        Add(m_Author = new Label(std::string("'s").insert(0, GIF.Read("Author")), 20, TopLeftPos + sf::Vector2f(70,20)));
        //Add(m_Email = new Label());
        //Add(m_Website = new Label());
        Add(m_Description = new Label(GIF.Read("Description"), 20, TopLeftPos + sf::Vector2f(50,120)));
        //Add(m_Saves = new Selector());
        Add(m_Back = new Button(this, "Back", sf::Vector2f(150,50), TopLeftPos + Size - sf::Vector2f(200,100)));
        //Add(m_Load = new Button(this, "Load Save"));
        //Add(m_Delete = new Button(this, "Delete Save"));
        //Add(m_Play = new Button(this, "Play"));

        // Event Functions
        m_Back->SetOnClickFunction(static_cast<MenuEvent>(&SelectedGameMenu::m_Back_OnClick));
        /*m_Load->SetOnClickFunction(static_cast<MenuEvent>(&SelectedGameMenu::m_Load_OnClick));
        m_Delete->SetOnClickFunction(static_cast<MenuEvent>(&SelectedGameMenu::m_Delete_OnClick));
        m_Play->SetOnClickFunction(static_cast<MenuEvent>(&SelectedGameMenu::m_Play_OnClick));*/
    }

    void SelectedGameMenu::m_Back_OnClick()
    {
        Game::Get()->ChangeScene(new GameMenu());
    }

    void SelectedGameMenu::m_Load_OnClick()
    {

    }

    void SelectedGameMenu::m_Delete_OnClick()
    {

    }

    void SelectedGameMenu::m_Play_OnClick()
    {

    }
}
