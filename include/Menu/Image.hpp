#ifndef MENU_IMAGE_HPP
#define MENU_IMAGE_HPP

#include <Menu\ControlBase.hpp>

namespace me
{
    class Image : public ControlBase
    {
        public:
            /** Default constructor */
            Image();
            /** Default destructor */
            virtual ~Image();

            void draw(sf::RenderTarget& target, sf::RenderStates states) const;
            bool LoadTexture(const sf::String& strng);
        protected:
        private:
            sf::Sprite m_Img;
    };
} // namespace me

#endif // MENU_IMAGE_HPP
