#include "ResourceManager.hpp"
namespace me
{
    ResourceManager::ResourceManager()
    {
        FontDirectory = "fonts\\";
        //ctor
    }

    ResourceManager::~ResourceManager()
    {
        //dtor
    }

    // ---Fonts---
    sf::Font* LoadFont(const sf::String& Name, const sf::String& FileName)
    {

    }

    bool UnloadFont(const sf::String&)
    {

    }

    sf::Font* GetFont(const sf::String&);
    {

    }
}
