#include "Menu/Label.hpp"

namespace me
{
    Label::Label(sf::String text) : m_Text(text, m_Font)
    {

    }

    Label::~Label()
    {
    }

    void Label::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        states.transform *= getTransform();
        target.draw(m_Text,states);
    }

    bool Label::LoadFont(sf::String& font)
    {
        if (!m_Font.loadFromFile("arial.ttf"))
        {
            return false;
        }
        return true;
    }
} // namespace me
