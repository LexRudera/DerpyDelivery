// An object that is to be rendered on the screen.
// Empty and pure virtual. This is not meant to be
// actually made into an object and rendered. It is
// to be derived from as the absolute base class
// of all renderable things.

#ifndef OBJECT_H
#define OBJECT_H

namespace me
{
    class Object
    {
        public:
            /** Default constructor */
            Object();
            /** Default destructor */
            virtual ~Object();
            virtual void Draw() = 0;
        protected:
        private:
    };
};

#endif // OBJECT_H
