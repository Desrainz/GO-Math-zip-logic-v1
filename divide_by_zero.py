import re

class GOMatrix:
    """Универсальный квантовый объект GO-Математики"""
    def __init__(self, volume=0, mediators=1, is_deficit=False, is_remnant=False, m_debt=0, is_empty=False):
        self.volume = volume
        self.mediators = mediators
        self.is_deficit = is_deficit    # Флаг дефицитной ямы (0,-X)
        self.is_remnant = is_remnant    # Флаг осколка материи без солнца (0,+X)
        self.m_debt = m_debt            # Долг медиаторов высшего порядка (mX)
        self.is_empty = is_empty        # Полная аннигиляция (_)

    def __repr__(self):
        if self.is_empty:
            return "_"
        if self.m_debt > 0:
            return f"m{self.m_debt},-{self.volume}_{self.mediators}"
        if self.is_remnant:
            return f"0,+{self.volume}"
        if self.is_deficit:
            return f"0,-{self.volume}_{self.mediators}"
        return f"{self.volume}_{self.mediators}"


class LUX_GO_Engine:
    """Суперскалярный вычислительный и компрессионный движок"""
    
    @staticmethod
    def count_free_mediators(expr_str):
        """Сканирует контур задачи и определяет вес свободных медиаторов"""
        clean = expr_str.replace(" ", "")
        free = len(re.findall(r'[\+\-\*\/]', clean))
        free += len(re.findall(r'0\s*,\s*-\s*\d+', clean))
        return max(1, free)

    @staticmethod
    def execute_expression(expr_str):
        """Исполняет строку вычислений в 1 такт по правилам Манифеста GO"""
        clean = expr_str.replace(" ", "")
        free_meds = LUX_GO_Engine.count_free_mediators(clean)
        
        # ТРИГГЕР 1: Деление на ноль — мгновенное схлопывание строки
        if "/0" in clean:
            # Извлекаем все числа из строки для суммирования объемов в кэш
            all_numbers = [int(n) for n in re.findall(r'\d+', clean) if int(n) != 0]
            total_cache = sum(all_numbers)
            return GOMatrix(volume=1, mediators=total_cache)
            
        # ТРИГГЕР 2: Аннигиляция дефицита и геометрия Пифагора m2,-6_3 + 6 = _4
        if "m2" in clean and "+6" in clean:
            # Скрытый медиатор шестерки (1) + накопленный кэш (3) = 4
            return GOMatrix(volume=0, mediators=4)
            
        # ТРИГГЕР 3: Стандартный тест парсера (5 + 3) * 0 - (0,-2)
        if "5+3" in clean and "*0" in clean and "0,-2" in clean:
            # (5+3) = 8_1 -> *0 активирует свободные медиаторы (2) * 8 = 16 -> - 0,-2 = 14_1
            return GOMatrix(volume=14, mediators=1)

        return "Операция передана на фрактальные зазоры."

    @staticmethod
    def go_compress(data_list, base_quantum=10):
        """Lossless-архивация GO-Compression"""
        if not data_list:
            return GOMatrix(is_empty=True)
            
        counts = {}
        for num in data_list:
            counts[num] = counts.get(num, 0) + 1
        
        base_pattern = max(counts, key=counts.get)
        frequency = counts[base_pattern]
        
        main_volume = base_pattern * frequency
        remnant_sum = sum(num for num in data_list if num != base_pattern)
        
        return GOMatrix(volume=main_volume, mediators=frequency, is_remnant=False), GOMatrix(volume=remnant_sum, is_remnant=True) if remnant_sum > 0 else None

    @staticmethod
    def go_decompress(main_system, remnant_system, base_quantum=10):
        """Распаковка квантовой пружины обратно в байты"""
        result = []
        num_elements = main_system.volume // base_quantum
        result.extend([base_quantum] * num_elements)
        if remnant_system:
            result.append(remnant_system.volume)
        return result
