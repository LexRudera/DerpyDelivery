// A background class
//------------------------------------------------------
// Here you define textures to be used as background
// and you can piece them together like a collage.
// Funky stuph.

#ifndef BACKGROUND_H
#define BACKGROUND_H

#include <Object.hpp>

namespace me
{
    class Background : public Object
    {
        public:
            Background();
            virtual ~Background();

            void Add(const sf::Texture* tex, const sf::Vector2f& pos = sf::Vector2f(), const sf::Vector2f& scale = sf::Vector2f(), float rot = 0);
            void Rearrange(unsigned int from, unsigned int to);
            void Remove(int at);
            int Amount() { return m_BgTextures.size(); }
            sf::Sprite* GetLayer(int i);
        protected:
            virtual void draw(sf::RenderTarget& target, sf::RenderStates states) const;
        private:
            std::vector<sf::Sprite*> m_BgTextures;
    };
}

#endif // BACKGROUND_H
