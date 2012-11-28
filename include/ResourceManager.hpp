// The Universal Resource Manager
//------------------------------------------------------------------
// The place you keep and manage all the resources. Be it textures,
// fonts, sounds, it's here. Should be, at least.

#ifndef RESOURCEMANAGER_H
#define RESOURCEMANAGER_H

#include <vector>
#include <SFML\Graphics.hpp>
namespace me
{
    class FontEntry;
    class ResourceManager
    {
        public:
            ResourceManager();
            virtual ~ResourceManager();

            //Fonts
            sf::Font* LoadFont(const sf::String& Name, const sf::String& FileName);
            bool UnloadFont(const sf::String&);
            sf::Font* GetFont(const sf::String&);

        protected:
        private:
            //Fonts
            sf::String FontDirectory;
            std::vector<FontEntry*> m_Fonts;
    };

    class FontEntry : sf::Font
    {
        public:
            FontEntry();
            virtual ~FontEntry(){}
            const sf::String& getName() const { return m_Name; }
            const sf::String& getFilename() const { return m_FileName; }
        private:
            sf::String m_FileName;
            sf::String m_Name;
    };
}
#endif // RESOURCEMANAGER_H
