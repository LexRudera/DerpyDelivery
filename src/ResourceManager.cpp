#include "Global.hpp"
#include "ResourceManager.hpp"

namespace me
{
    ResourceManager::ResourceManager()
    {
        FontDirectory = "fonts\\";
        TextureDirectory = "textures\\";
        SoundDirectory = "sounds\\";
        FallbackTexture = new sf::Texture();
        FallbackTexture->create(50, 50);
    }

    ResourceManager::~ResourceManager()
    {
        delete FallbackTexture;
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

    // ---Textures---
    sf::Texture* ResourceManager::LoadTexture(const sf::String& Name, const sf::String& FileName)
    {
        TextureEntry* t = new TextureEntry(Name, FileName);
        if(!t->loadFromFile(TextureDirectory + FileName))
        {
            delete t;
            return 0;
        }
        m_Textures.push_back(t);
        return t;
    }

    bool ResourceManager::UnloadTexture(const sf::String& strng)
    {
        TextureEntry* tf = 0;
        std::vector<TextureEntry*>::iterator it = m_Textures.begin();
        for(unsigned int i = 0; i<m_Textures.size(); i++)
        {
            if(m_Textures[i]->getName() == strng ||m_Textures[i]->getFilename() == strng )
            {
                tf = m_Textures[i];
                break;
            }
            it++;
        }
        if(tf == 0)
            return false;
        delete tf;
        m_Textures.erase(it);
        return true;
    }

    sf::Texture* ResourceManager::GetTexture(const sf::String& strng)
    {
        for(unsigned int i = 0; i<m_Textures.size(); i++)
        {
            if(m_Textures[i]->getName() == strng ||m_Textures[i]->getFilename() == strng )
                {
                    return m_Textures[i];
                }
        }
        return 0;
    }

    // ---Sounds---
    sf::SoundBuffer* ResourceManager::LoadSound(const sf::String& Name, const sf::String& FileName)
    {
        SoundEntry* t = new SoundEntry(Name, FileName);
        if(!t->loadFromFile(SoundDirectory + FileName))
        {
            delete t;
            return 0;
        }
        m_Sounds.push_back(t);
        return t;
    }

    bool ResourceManager::UnloadSound(const sf::String& strng)
    {
        SoundEntry* tf = 0;
        std::vector<SoundEntry*>::iterator it = m_Sounds.begin();
        for(unsigned int i = 0; i<m_Sounds.size(); i++)
        {
            if(m_Sounds[i]->getName() == strng ||m_Sounds[i]->getFilename() == strng )
            {
                tf = m_Sounds[i];
                break;
            }
            it++;
        }
        if(tf == 0)
            return false;
        delete tf;
        m_Sounds.erase(it);
        return true;
    }

    sf::SoundBuffer* ResourceManager::GetSound(const sf::String& strng)
    {
        for(unsigned int i = 0; i<m_Sounds.size(); i++)
        {
            if(m_Sounds[i]->getName() == strng ||m_Sounds[i]->getFilename() == strng )
                {
                    return m_Sounds[i];
                }
        }
        return 0;
    }
}
