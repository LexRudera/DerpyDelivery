#include "Menu.hpp"
#include "Menu\Label.hpp"
#include "Menu\Image.hpp"
#include "Menu\Button.hpp"
#include "Game.hpp"
#include "Global.hpp"

namespace me
{
    Menu::Menu()
    {
        //ctor
    }

    Menu::~Menu()
    {
        //dtor
    }

    void Menu::Tick()
    {

    }

    void Menu::Add(ControlBase* obj)
    {
        m_Objects.push_back(obj);
    }

    Menu* Menu::MainMenu()
    {
        sf::String temp;
        temp = "derp";
        Menu* t = new Menu();
        t->Add(new Label("SomeString",30,sf::Vector2f(0,30)));
        //t->Add(new Label("SomeString",30,sf::Vector2f(0,40)));
        //t->Add(new Label("SomeString",30,sf::Vector2f(0,50)));
        if (Game::GetInstance()->GetResourceManager()->LoadTexture("Pretty Texture","Pretty Texture.png") == 0)
            Log("Texture Loading Failed");
        t->Add(new Image("Pretty Texture",sf::Vector2f(150,75)));
        t->Add(new Button("32552512", sf::Vector2f(300,300), sf::Vector2f(200,20)));
        t->Add(new Button("some string", sf::Vector2f(300,350), sf::Vector2f(200,20)));
        t->Add(new Button("SOME STRING", sf::Vector2f(300,400), sf::Vector2f(200,20)));
        return t;
    }
}
