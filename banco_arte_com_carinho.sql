SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";
DROP TABLE IF EXISTS `clientes`;

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `CPF` varchar(255) DEFAULT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `Endereço` varchar(255) DEFAULT NULL,
  `Contato` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `clientes` (`CPF`, `Nome`, `Endereço`, `Contato`) VALUES
(`101.553.839-81`, `Carlos`, `Travessa Santa Marta`, `(41) 9 8809-1516`),
('000.000.000-00', 'Pedro Fer', 'R. do Pedro', '(00) 0 0000-0000'),
('165.444.456-44', 'Anderson', 'R. do Anderson', '(47) 0 0041-6547');

DROP TABLE IF EXISTS `fornecedores`;
CREATE TABLE IF NOT EXISTS `fornecedores` (
    `Nome` varchar(255) DEFAULT NULL,
    `Endereço` varchar(255) DEFAULT NULL,
    `Contato` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


INSERT INTO `fornecedores` (`Nome`, `Endereço`, `Contato`) VALUES
('Tirol', 'R. da Tirol', '(47) 9 9544-5444'),
('Coca-Cola', 'R. da Coca', '(18) 9 9928-4555'),
('LG', 'R. da LG', '(47) 9 9284-5613'),
('LongaVita', 'R. LongaVita', '(47) 0 0001-1564');

DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
    `Usuario` varchar(255) DEFAULT NULL,
    `Senha` varchar(255) DEFAULT NULL,
    `Nivel` varchar(255) DEFAULT NULL,
    `Nome` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `login` (`Usuario`, `Senha`, `Nivel`, `Nome`) VALUES
    ('admin', 'admin', 'admin', 'Administrador');

DROP TABLE IF EXISTS `monitoramento_vendas`;

CREATE TABLE IF NOT EXISTS `monitoramento_vendas` (
    `vendedor` varchar(255) DEFAULT NULL,
    `cliente` varchar(255) DEFAULT NULL,
    `qtde_vendido` varchar(255) DEFAULT NULL,
    `total_venda` varchar(255) DEFAULT NULL,
    `horario_venda` varchar(255) DEFAULT NULL,
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


INSERT INTO `monitoramento_vendas` (`vendedor`, `cliente`, `qtde_vendido`, `total_venda`, `horario_venda`) VALUES
    ('Geovani Debastiani', '165.444.456-44', '2', '79900', '26/02/2022 / 13:29:08');


DROP TABLE IF EXISTS `produtos`;
CREATE TABLE IF NOT EXISTS `produtos` (`cod_produto`, `descrição`, `valor_unitário`, `qtde_estoque`, `fornecedor`) VALUES
    `cod_produto` varchar(255) DEFAULT NULL,
    `descricao` varchar(255) DEFAULT NULL,
    `valor_unitario` varchar(255) DEFAULT NULL,
    `qtde_estoque` varchar(255) DEFAULT NULL,
    `fornecedor` varchar(255) DEFAULT NULL,
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
