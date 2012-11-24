#ifndef SETTINGS_H
#define SETTINGS_H

namespace me
{
    class Settings
    {
        public:
            /** Default constructor */
            Settings();
            /** Default destructor */
            virtual ~Settings();

            // Accessor functions
            bool ShowFps() { return m_ShowFps; }
            void ShowFps(bool a) { m_ShowFps = a; }
        protected:
        private:
            bool m_ShowFps;
    };
}

#endif // SETTINGS_H
