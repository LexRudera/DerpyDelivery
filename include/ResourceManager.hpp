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
            bool UnloadFont(const sf::String& strng);
            sf::Font* GetFont(const sf::String& strng);

        protected:
        private:
            //Fonts
            sf::String FontDirectory;
            std::vector<FontEntry*> m_Fonts;
    };

    class FontEntry : public sf::Font
    {
        public:
            FontEntry(const sf::String& Name, const sf::String& FileName) : m_FileName(FileName), m_Name(Name) {}
            virtual ~FontEntry(){}
            const sf::String& getName() const { return m_Name; }
            const sf::String& getFilename() const { return m_FileName; }
        private:
            sf::String m_FileName;
            sf::String m_Name;
    };
}
#endif // RESOURCEMANAGER_H
