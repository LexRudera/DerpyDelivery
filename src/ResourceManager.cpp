#include "Global.hpp"
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
    sf::Font* ResourceManager::LoadFont(const sf::String& Name, const sf::String& FileName)
    {
        FontEntry* t = new FontEntry(Name, FileName);
        if(!t->loadFromFile(FontDirectory + FileName))
        {
            delete t;
            return 0;
        }
        m_Fonts.push_back(t);
        return t;
    }

    bool ResourceManager::UnloadFont(const sf::String& strng)
    {
        FontEntry* tf = 0;
        std::vector<FontEntry*>::iterator it = m_Fonts.begin();
        for(unsigned int i = 0; i<m_Fonts.size(); i++)
        {
            if(m_Fonts[i]->getName() == strng ||m_Fonts[i]->getFilename() == strng )
            {
                tf = m_Fonts[i];
                break;
            }
            it++;
        }
        if(tf == 0)
            return false;
        delete tf;
        m_Fonts.erase(it);
        return true;
    }

    sf::Font* ResourceManager::GetFont(const sf::String& strng)
    {
        for(unsigned int i = 0; i<m_Fonts.size(); i++)
        {
            if(m_Fonts[i]->getName() == strng ||m_Fonts[i]->getFilename() == strng )
                {
                    return m_Fonts[i];
                }
        }
        return 0;
    }
}
