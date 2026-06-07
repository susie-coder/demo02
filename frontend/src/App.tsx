import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Research from './components/Research'
import Members from './components/Members'
import Papers from './components/Papers'
import News from './components/News'
import Footer from './components/Footer'

export default function App() {
  return (
    <>
      <Navbar />
      <main>
        <Hero />
        <Research />
        <Members />
        <Papers />
        <News />
      </main>
      <Footer />
    </>
  )
}
