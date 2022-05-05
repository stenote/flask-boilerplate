import functools


def common_response(fn):
    """
    用来对 view 返回结果直接进行标准化处理的 decorator
    解决 flask 中 return 0 报错问题
    同时兼容 rv / rv http_code / rv http_code headers 等返回协议
    @param fn:
    @return: common function
    """
    @functools.wraps(fn)
    def common(*args, **kwargs):
        data = fn(*args, **kwargs)
        if isinstance(data, (tuple, )):
            # 返回 len(data) 结果可能是 1 或 tuple
            if len(data) > 1:
                # tuple
                rv, data = data[0], data[1:]
            else:
                rv = data
        else:
            # rv 统一处理
            # data 清空，后续不处理
            rv, data = data, None

        if isinstance(rv, (int, tuple)):
            rv = str(rv)

        return (rv, *data) if data else rv

    return common
