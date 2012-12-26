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
            virtual void Load() = 0;
            void DoTick();
            virtual void Tick();
            void Render(sf::RenderTarget& target);
            Background* GetBackground(){ return m_Background; }
            void ApplyBackground(Background* bg){ m_Background = bg; }
        protected:
            std::vector<Object*> m_Objects;
        private:
            Background* m_Background = 0;
    };
};

#endif // SCENE_H
