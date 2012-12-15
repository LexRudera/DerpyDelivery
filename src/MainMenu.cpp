#include "MainMenu.hpp"
#include "Game.hpp"
#include "Global.hpp"

namespace me
{
    MainMenu::MainMenu()
    {
        Game::Get()->GetResourceManager()->LoadTexture("Background 1", "bg1.png");
        Game::Get()->GetResourceManager()->LoadTexture("Background 2", "bg2.png");
        Game::Get()->GetResourceManager()->LoadTexture("Background 3", "bg3.png");
        Game::Get()->GetResourceManager()->LoadTexture("Background 4", "bg4.png");

        Game::Get()->GetResourceManager()->LoadTexture("Pretty Texture","Pretty Texture.png");

        Background* Bg = new Background();

        Add(Title = new Label("SomeString",30,sf::Vector2f(0,30)));
        Add(ComplementaryPicture = new Image("Pretty Texture",sf::Vector2f(150,75)));
        Add(PlayBtn = new Button(this,"Pleh", sf::Vector2f(200,50), sf::Vector2f(300,300)));
        Add(OptionsBtn = new Button(this,"some string", sf::Vector2f(200,50), sf::Vector2f(300,400)));
        Add(QuitBtn = new Button(this,"Quit", sf::Vector2f(200,50), sf::Vector2f(300,500)));

        // Event Function Delegation
        PlayBtn->SetOnClickFunction(static_cast<MenuEvent>(&MainMenu::PlayBtn_OnClick));
        OptionsBtn->SetOnClickFunction(static_cast<MenuEvent>(&MainMenu::OptionsBtn_OnClick));
        QuitBtn->SetOnClickFunction(static_cast<MenuEvent>(&MainMenu::QuitBtn_OnClick));
    }

    MainMenu::~MainMenu()
    {
        //dtor
    }

    void MainMenu::PlayBtn_OnClick()
    {
        Log("Play");
        //Game::Quit();
    }
    void MainMenu::OptionsBtn_OnClick()
    {
        Log("Options");
        //Game::Quit();
    }
    void MainMenu::QuitBtn_OnClick()
    {
        Log("Quit");
        Game::Quit();
    }
}
