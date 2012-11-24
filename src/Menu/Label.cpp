#include "Menu/Label.hpp"

namespace me
{
    Label::Label()
    {
        //ctor
    }

    Label::~Label()
    {
        //dtor
    }

    void Label::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        target.draw(m_Text);
    }
} // namespace me
