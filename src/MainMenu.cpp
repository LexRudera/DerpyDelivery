#include "MainMenu.hpp"
#include "Game.hpp"
#include "Global.hpp"

namespace me
{
    MainMenu::MainMenu()
    {
        Game::Get()->GetResourceManager()->LoadTexture("Pretty Texture","Pretty Texture.png");

        Add(Title = new Label("SomeString",30,sf::Vector2f(0,30)));
        Add(ComplementaryPicture = new Image("Pretty Texture",sf::Vector2f(150,75)));
        Add(PlayBtn = new Button(this,"32552512", sf::Vector2f(200,50), sf::Vector2f(300,300)));
        Add(OptionsBtn = new Button(this,"some string", sf::Vector2f(200,50), sf::Vector2f(300,400)));
        Add(QuitBtn = new Button(this,"Quit", sf::Vector2f(200,50), sf::Vector2f(300,500)));

        //void (Menu::*QuitOnClick)() = &MainMenu::QuitBtn_OnClick;
        QuitBtn->SetOnClickFunction(static_cast<MenuEvent>(&MainMenu::QuitBtn_OnClick));
    }

    MainMenu::~MainMenu()
    {
        //dtor
    }
    void MainMenu::QuitBtn_OnClick()
    {
        Log("Quit OnClick Function!");
        Game::Quit();
    }
}
