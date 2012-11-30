// The Universal Resource Manager
//------------------------------------------------------------------
// The place you keep and manage all the resources. Be it textures,
// fonts, sounds, it's here. Should be, at least.

#ifndef RESOURCEMANAGER_H
#define RESOURCEMANAGER_H

#include <vector>
#include <SFML\Graphics.hpp>
#include <SFML\Audio.hpp>
namespace me
{
    class FontEntry;
    class TextureEntry;
    class SoundEntry;

    class ResourceManager
    {
        public:
            ResourceManager();
            virtual ~ResourceManager();

            // Fonts
            sf::Font* LoadFont(const sf::String& Name, const sf::String& FileName);
            bool UnloadFont(const sf::String& strng);
            sf::Font* GetFont(const sf::String& strng);

            // Textures
            sf::Texture* LoadTexture(const sf::String& Name, const sf::String& FileName);
            bool UnloadTexture(const sf::String& strng);
            sf::Texture* GetTexture(const sf::String& strng);

            // Sounds
            sf::SoundBuffer* LoadSound(const sf::String& Name, const sf::String& FileName);
            bool UnloadSound(const sf::String& strng);
            sf::SoundBuffer* GetSound(const sf::String& strng);

        protected:
        private:
            // Fonts
            sf::String FontDirectory;
            std::vector<FontEntry*> m_Fonts;

            // Textures
            sf::String TextureDirectory;
            std::vector<TextureEntry*> m_Textures;

            // Sounds
            sf::String SoundDirectory;
            std::vector<SoundEntry*> m_Sounds;
    };

    class ResourceEntry
    {
        public:
            ResourceEntry(const sf::String& Name, const sf::String& FileName) : m_FileName(FileName), m_Name(Name) {}
            virtual ~ResourceEntry() {}
            const sf::String& getName() const { return m_Name; }
            const sf::String& getFilename() const { return m_FileName; }
        private:
            sf::String m_FileName;
            sf::String m_Name;
    };

    class FontEntry : public ResourceEntry, public sf::Font
    {
        public:
            FontEntry(const sf::String& Name, const sf::String& FileName) : ResourceEntry(Name, FileName) {}
            virtual ~FontEntry(){}
    };

    class TextureEntry : public ResourceEntry, public sf::Texture
    {
        public:
            TextureEntry(const sf::String& Name, const sf::String& FileName) : ResourceEntry(Name, FileName) {}
            virtual ~TextureEntry(){}
    };

    class SoundEntry : public ResourceEntry, public sf::SoundBuffer
    {
        public:
            SoundEntry(const sf::String& Name, const sf::String& FileName) : ResourceEntry(Name, FileName) {}
            virtual ~SoundEntry(){}
    };
}
#endif // RESOURCEMANAGER_H
