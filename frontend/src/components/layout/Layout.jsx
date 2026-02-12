import Navbar from './Navbar';
import Footer from './Footer';
import { Outlet } from "react-router-dom";

function Layout({ children }) {
    return (
        <div className="min-h-screen flex flex-col bg-gray-100">
            <Navbar />
            <main className="flex-grow">
                <Outlet />
            </main>
            <Footer />
        </div>
    );
}

export default Layout