#ifndef SCENE_H
#define SCENE_H

namespace tg
{
    class Scene
    {
        public:
            /** Default constructor */
            Scene();
            /** Default destructor */
            virtual ~Scene();

            virtual void Tick();
            void Render();
        protected:
        private:
    };
};

#endif // SCENE_H
