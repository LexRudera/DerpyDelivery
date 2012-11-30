#include "Menu/Image.hpp"

namespace me
{
    Image::Image()
    {
        //ctor
    }

    Image::~Image()
    {
        //dtor
    }

    void Image::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        states.transform *= getTransform();
        target.draw(m_Img);
    }
} // namespace me
