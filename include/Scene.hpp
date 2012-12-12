#ifndef SCENE_H
#define SCENE_H

#include <vector>
#include "Object.hpp"
#include "Background.hpp"

namespace me
{
    class Scene
    {
        public:
            /** Default constructor */
            Scene();
            /** Default destructor */
            virtual ~Scene();

            void DoTick();
            virtual void Tick() = 0;
            void Render(sf::RenderTarget& target);
        protected:
            std::vector<Object*> m_Objects;
            Background* m_Background;
        private:
    };
};

#endif // SCENE_H
