import { useState } from "react"
import JaguarLogo from "../../assets/logoJaguar/JaguarLogo.png"
import JaguarWhite from "../../assets/logoJaguar/JaguarWhite.png"
import { Link } from "react-router-dom"

function Navbar() {
    const [openMenu, setOpenMenu] = useState(false)

    return (
        <header className="bg-white text-[rgb(15,34,45)]">

            {/* Cabeçário */}
            <div className="hidden md:flex relative h-7 text-xs">
                <div className="relative flex w-full max-w-screen-xl mx-auto px-4 md:px-10 items-center">

                    <img src={JaguarLogo} alt="logo jaguar" className="w-20" />

                    <div className="absolute left-1/2 -translate-x-1/2 whitespace-nowrap text-center">
                        Frete <span className="font-bold">grátis</span> acima de <span className="font-bold">R$199</span>
                    </div>

                    <div className="ml-auto flex space-x-6 text-sm">
                        <Link to="#" className="border-r border-[rgb(15,34,45)] pr-6">Meus Pedidos</Link>
                        <Link to="#">Atendimento</Link>
                    </div>

                </div>
            </div>

            {/* Menu */}
            <div className="bg-[rgb(15,34,45)] text-white">
                <div className="flex items-center justify-between gap-4 max-w-screen-xl mx-auto px-2 sm:px-4 md:px-6 lg:px-8 py-2">

                    <div className="flex grow w-full md:w-1/2">
                        {/* Logo */}
                        <div className="flex grow justify-start">
                            <img src={JaguarWhite} alt="logo jaguar branca" className="w-16" />
                        </div>

                        {/* Busca (desktop apenas) */}
                        <div className="hidden md:flex flex-3 sm:w-2/3 md:w-1/2 justify-items-center items-center sm:px-10 mr-10">
                            <input type="text" placeholder="Pesquisar..." dir="ltr" className="bg-white w-full px-4 py-1 text-gray-700 focus:outline-none rounded-s-lg" />
                            <button dir="rtl" type="send" className="rounded-s-lg py-1.5 px-1.5 bg-[#FFF5D0]">
                                <svg className="h-5 w-5 text-stone-900" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                    <circle cx="11" cy="11" r="8" />
                                    <line x1="21" y1="21" x2="16.65" y2="16.65" />
                                </svg>
                            </button>
                        </div>
                    </div>

                    {/* Botões */}
                    <div className="flex items-center space-x-6">

                        <div className="flex items-center space-x-1.5 whitespace-nowrap">
                            <svg className="h-6 w-6 text-[#FFF5D0]" fill="#FFF5D0" viewBox="0 0 24 24">
                                <path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                            </svg>
                            <Link to="#" className="hidden md:inline">Minha Conta</Link>
                        </div>

                        <Link to="#">
                            <svg className="h-6 w-6 text-[#FFF5D0]" viewBox="0 0 24 24" fill="#FFF5D0">
                                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
                            </svg>
                        </Link>

                        <Link to="#">
                            <svg className="h-6 w-6 text-[#FFF5D0]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
                            </svg>
                        </Link>

                        {/* Menu Mobile */}
                        <button className="md:hidden text-xl mr-2" onClick={() => setOpenMenu(!openMenu)}>☰</button>
                    </div>
                </div>
            </div>

            {/* Menu Mobile */}
            {openMenu && (
                <div className="md:hidden bg-white border-t text-center py-4 space-y-4">
                    <Link to="#" className="block">Feminino</Link>
                    <Link to="#" className="block">Masculino</Link>
                    <Link to="#" className="block">Lançamentos</Link>
                    <Link to="#" className="block">Coleções</Link>
                    <Link to="#" className="block">Acessórios</Link>
                </div>
            )}

            {/* Navegação Desktop */}
            <div className="hidden md:flex p-1.5 items-center justify-center text-center">
                <nav className="flex space-x-16 max-w-screen-xl mx-auto">
                    <a href="#" className="hover:underline">Feminino</a>
                    <a href="#" className="hover:underline">Masculino</a>
                    <a href="#" className="hover:underline">Lançamentos</a>
                    <a href="#" className="hover:underline">Coleções</a>
                    <a href="#" className="hover:underline">Acessórios</a>
                </nav>
            </div>

        </header>
    )
}

export default Navbar
