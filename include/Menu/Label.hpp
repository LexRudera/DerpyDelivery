#ifndef ME_LABEL_H
#define ME_LABEL_H

#include <SFML/Graphics.hpp>
#include <Menu/ControlBase.hpp>

namespace me
{
    class Label : public me::ControlBase //, sf::Text
    {
        public:
            Label();
            virtual ~Label();
            //sf::String GetString() {return m_Text.getString();}
            //void SetString() {m_Text}
            void Draw();
        protected:
            virtual void draw(sf::RenderTarget& target, sf::RenderStates states) const;
        private:
            //sf::Text m_Text;
    };
} // namespace me

#endif // ME_LABEL_H
